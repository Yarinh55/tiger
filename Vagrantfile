Vagrant.configure("2") do |config|
  config.vm.box = "fedora/30-cloud-base"
  config.vm.provision "shell", path:"scripts/bootstrap.sh"
  config.vm.network "forwarded_port", guest: 5000, host: 5000 
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
  end
mysql -u root -p passwd -e "INSERT INTO tiger.users (username,password) VALUES('YarinMor','RandomPass123545');"
mysql -u root -p passwd -e "INSERT INTO tiger.messages (username,create_date,content) VALUES ('YarinMor','2020-01-01 10:10:10','This is my first message,Hello world');"
end
