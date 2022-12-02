def controller(host,user,password):
    contenido = open("Inventories/template.txt").read().splitlines()
    contenido.insert(6,"            "+host)
    contenido.remove("            host")
    contenido.insert(9,"        ansible_user: "+user)
    contenido.remove("        ansible_user: master")
    contenido.insert(10,"        ansible_ssh_pass: "+password)
    contenido.remove("        ansible_ssh_pass: m1")
    f = open('Inventories/import_inventory.yml', "w")
    f.writelines("\n".join(contenido))
controller('10.89.105.98','master','m1')

# ansible-playbook playbooks/os4690/Install_Controller.yml -vv  -i Inventories/import_inventory.yml -e 'level_complement=V8R1SP2.j292.1-20221111.223820-1 opc=1 ASM=Accept level_name=V8R1SP2.j292.1 level_complementEPS=V8R1SP2.j292.1-20221111.223829-1' 2>&1 | tee temp.txt

# - name: Printing opc ACE3D
#   shell: "echo {{opc}} >> {{c_adx_imnt}}UINSTALL/START3D.BAT"

# - name: Printing opc ACE4D
#   shell: "echo {{opc}} >> {{c_adx_imnt}}UINSTALL/START4D.BAT"
