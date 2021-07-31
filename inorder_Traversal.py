def inorder(result, no):
    if no != None:
        inorder(result, no.left)
        result.append(no.value)
        inorder(result, no.right)



    
