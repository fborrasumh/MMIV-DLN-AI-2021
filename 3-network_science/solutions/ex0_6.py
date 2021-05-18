
def ba(n,m):
    A = np.zeros((n,n))
    
    k_sum = np.zeros(n)
    for node in range(n):
        # add m new links
        if node < m: 
            # can only add node number of links
            A[node, :node], A[:node, node] = 1,1
            k_sum += node*2
        else:
            #randomly add m new links
            probs = A.sum(1) / k_sum
            idx = np.random.choice(range(node), size=m, p=probs[:node], replace=False)
            A[node,idx], A[idx, node] = 1,1
            k_sum += 2*m
    return A