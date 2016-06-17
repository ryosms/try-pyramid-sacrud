# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "geerlingguy/centos7"
  config.vm.box_url = "https://atlas.hashicorp.com/geerlingguy/boxes/centos7"
  
  # synced fonder
  config.vm.synced_folder ".", "/vagrant", :mount_options => ['dmode=775', 'fmode=664']

  config.vm.network :forwarded_port, guest: 6543, host: 6543
  config.vm.network :forwarded_port, guest: 8080, host: 8080
  # Enable Provisioning
  config.vm.provision :shell, path: "./provisioning.sh"
end
