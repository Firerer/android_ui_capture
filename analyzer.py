from lxml import etree

p1 = 'results/1647395109/phone.xml'
p2 = 'results/1647395182/phone.xml'
t1 = 'results/1647395109/tablet.xml'

def element_simlar_rate(e1, e2):
	n = 0
	total = 0
	keys = e1.attrib.iterkeys()
	for k in keys:
		total += 1
		print(f'comparing {k}')
		if e2.attrib.has_key(k):
			v1 = e1.attrib.get(k)
			v2 = e2.attrib.get(k)
			if v1 == v2:
				n += 1
	return n / total

tree1 = etree.parse(p1)
tree2 = etree.parse(t1)
# print(type(tree.getroot().attrib))
# print(etree.tostring(tree))
r = element_simlar_rate(tree1.getroot().child[0], tree2.getroot().child[0])
print(r)

