ansible-playbook playbooks/os4690/Install_Controller.yml -vv  -i Inventories/import_inventory.yml -e 'level_complement=V8R1SP2.j301-20221110.173537-1 opc=2 ASM=Test level_name=V8R1SP2.j301 level_complementEPS=V8R1SP2.j301-20221110.173550-1' 2>&1 | tee temp.txt