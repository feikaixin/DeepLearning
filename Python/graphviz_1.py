"类库graphviz的使用, 用于生成决策树、流程图效果拔群"

import graphviz

# node_attr更改节点的样式
dot = graphviz.Digraph(comment='The Round Table', node_attr={"shape": "plaintext"})

# 设置所有节点的样式
dot.attr("node", shape="rarrow")

dot.node(name='a',color='red')
dot.node(name='b',color='blue')
dot.node(name='c',color='blue')
dot.node(name='d',color='blue')
dot.edge('a','b',color='green', label="sd")
dot.edges(["ac", "bd"])

print(dot.source)
# 生成的pdf缓存png格式
dot.format = 'png'

dot.render('./gv/test-table.gv', view=True)

# Source从一个dot源码中进行渲染
graph = graphviz.Source(dot)
graph.view()