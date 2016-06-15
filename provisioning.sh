#!/usr/bin/env bash

if ! [ `which ansible` ]; then
    sudo yum install -y ansible
fi

chmod -x /vagrant/playbook/hosts
export PYTHONUNBUFFERED=1
ansible-playbook -i /vagrant/playbook/hosts /vagrant/playbook/provisioning.yml
