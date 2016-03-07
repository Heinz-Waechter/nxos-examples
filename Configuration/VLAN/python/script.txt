from .vlan import Vlan

#Mention vlan id to be created
vlan_id = 40

v = Vlan()
print "Before adding vlan"
print v.show_vlan().get_vlans()

print "\nCreating Vlan with vlan id %s" %vlan_id
v.create_vlan(vlan_id)

print "\nAfter adding vlan"
print v.show_vlan().get_vlans()

print "\nDeleting vlan with vlan id %s" %vlan_id
v.delete_vlan(vlan_id)

print "\nAfter deleting vlan id %s " %vlan_id
print v.show_vlan().get_vlans()

