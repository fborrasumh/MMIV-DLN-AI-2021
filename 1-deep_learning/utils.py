# From https://forums.fast.ai/t/plotting-metrics-after-learning/69937/3

from fastai.imports import *
from fastai.torch_core import *
from fastai.learner import *
from fastai.vision.all import *
    
@patch
@delegates(subplots)
def plot_metrics(self: Recorder, nrows=None, ncols=None, figsize=None, endnames=-1, **kwargs):
    metrics = np.stack(self.values)
    names = self.metric_names[1:endnames]
    n = len(names) - 1
    if nrows is None and ncols is None:
        nrows = int(math.sqrt(n))
        ncols = int(np.ceil(n / nrows))
    elif nrows is None: nrows = int(np.ceil(n / ncols))
    elif ncols is None: ncols = int(np.ceil(n / nrows))
    figsize = figsize or (ncols * 6, nrows * 4)
    fig, axs = subplots(nrows, ncols, figsize=figsize, **kwargs)
    axs = [ax if i < n else ax.set_axis_off() for i, ax in enumerate(axs.flatten())][:n]
    for i, (name, ax) in enumerate(zip(names, [axs[0]] + axs)):
        ax.plot(metrics[:, i], color='#1f77b4' if i == 0 else '#ff7f0e', label='valid' if i > 0 else 'train')
        ax.set_title(name if i > 1 else 'losses')
        ax.legend(loc='best')
    plt.show()
    
    
    
    
# CAM and grad-CAM for the tumor grade example, modified from fastai

class Hook():
    def __init__(self, m):
        self.hook = m.register_forward_hook(self.hook_func)   
    def hook_func(self, m, i, o): self.stored = o.detach().clone()
    def __enter__(self, *args): return self
    def __exit__(self, *args): self.hook.remove()

class HookBwd():
    def __init__(self, m):
        self.hook = m.register_backward_hook(self.hook_func)   
    def hook_func(self, m, gi, go): self.stored = go[0].detach().clone()
    def __enter__(self, *args): return self
    def __exit__(self, *args): self.hook.remove()
        

def get_cam(img_fn, dls, learn):
    img = PILImage.create(img_fn)
    x, = first(dls.test_dl([img]))
    _, _, sz, _ = x.shape
    x_dec = TensorImage(dls.train.decode((x,))[0][0])
    
    with Hook(learn.model[0]) as hook:
        with torch.no_grad(): 
            output = learn.model.eval()(x.cuda())
            act = hook.stored[0]
            
    cam_map = torch.einsum('ck,kij->cij', learn.model[1][-1].weight, act)

    
    _,ax = plt.subplots(1,2, figsize=(20,20))
    x_dec.show(ctx=ax[0])
    x_dec.show(ctx=ax[1])
    ax[1].imshow(cam_map[1].detach().cpu(), alpha=0.6, extent=(0,sz,sz,0),
              interpolation='bilinear', cmap='magma')
    ax[1].set_title('CAM')
    ax[0].set_title('orig')



def get_gradcam(img_fn, df, dls, learn, save=False):
    tcga_id = "-".join(img_fn.split("/")[-1].split("-")[:3])
    print(tcga_id)
    grade = df.loc[df['TCGA ID'] == tcga_id]['Grade'].values[0]
    img = PILImage.create(img_fn)
    x, = first(dls.test_dl([img]))
    _, _, sz, _ = x.shape
    x_dec = TensorImage(dls.train.decode((x,))[0][0])
    
    cls = 1
    with HookBwd(learn.model[0]) as hookg:
        with Hook(learn.model[0]) as hook:
            output = learn.model.eval()(x.cuda())
            act = hook.stored
        output[0,cls].backward()
        grad = hookg.stored
            
    w = grad[0].mean(dim=[1,2], keepdim=True)
    cam_map = (w * act[0]).sum(0)
    
    
    f,ax = plt.subplots(1,2, figsize=(30,15))
    f.suptitle(f'Subject {tcga_id}, grade {int(grade)}', fontsize=16)
    x_dec.show(ctx=ax[0])
    x_dec.show(ctx=ax[1])
    ax[1].imshow(cam_map.detach().cpu(), alpha=0.6, extent=(0,sz,sz,0),
              interpolation='bilinear', cmap='magma')
    ax[1].set_title('grad-CAM')
    ax[0].set_title('orig')
    
    plt.show()
    if save: f.savefig(f'{tcga_id}-gradcam.jpg')
        
        
        
# CAM and grad-CAM for the molecules example, modified from fastai

def get_mol_gradcam(instance, dls, learn):
    img, c = instance
    x,  = first(dls.test_dl([img]))
    _, _, sz, _ = x.shape

    cls = 1
    with HookBwd(learn.model[0]) as hookg:
        with Hook(learn.model[0]) as hook:
            output = learn.model.eval()(x.cuda())
            act = hook.stored
        output[0,cls].backward()
        grad = hookg.stored

    w = grad[0].mean(dim=[1,2], keepdim=True)
    cam_map = (w * act[0]).sum(0)
    
    x_dec = TensorImage(dls.train.decode((x,))[0][0])
    
    f,ax = plt.subplots(1,2, figsize=(10,6))
    f.suptitle(f'Activity {int(c)}', fontsize=16)
    x_dec.show(ctx=ax[0])
    x_dec.show(ctx=ax[1])
    ax[1].imshow(cam_map.detach().cpu(), alpha=0.6, extent=(0,sz,sz,0),
              interpolation='bilinear', cmap='magma')
    ax[1].set_title('grad-CAM')
    ax[0].set_title('orig')
    
    plt.show()
    