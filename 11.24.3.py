import inspect
def func(n):
    while n > 0:
        n -= 1
    
srclines = inspect.getsource(func).splitlines()
print(srclines)
src = '\n'.join(srclines[0:])
print(src)
src = 'if 1:\n' + src
print(src)
top = ast.parse(src, mode='exec')
print('top',top)

def visit_FunctionDef(node):
        #Compile some assignments to lower the constants
        code = '__globals = globals()\n'
        code += '\n'.join("{0} = __globals['{0}']".format(name) for name in self.lowered_names)
        code_ast = ast.parse(code, mode='exec')
        
        # Inject new statements into the function body
        node.body[:0] = code_ast.body
        
        # Save the function object
        func = node
        return func
        
visit_FunctionDef(top)
