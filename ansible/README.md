# Cai dat may ao vagrant

$ https://www.vagrantup.com/downloads.html

# Cai dat may ao vagrant

$ vagrant init ubuntu/trusty64

# Cau hinh may ao  theo file Vagrantfile

$ vagrant up

# Tai may chu chay cac lenh

$ ssh-keygen

$ cd ~/.ssh

$ > known_hosts

# Vao vagrant bang lenh

$ vagrant ssh

# coppy id_rsa.pub vao vagrant tai thu muc ~/.ssh/authorized_keys

# Muon vao lai vagrant thi chay lenh  
$ ssh vagrant@192.168.33.10

# Ve may chu, coppy doan code vao /opt/ansible/

# Sau do chay lenh

$ ansible-playbook -u vagrant -i hosts site.yml


----------------------------------------------------------------------
# Yeu cau: Viết 1 web app chạy ở port 80, nhận request HTTP request bất kỳ, đếm và trả ra số lượng unique user agent hiện tại (theo từng ngày)

Yêu cầu:

* Dùng flask, redis
* Tham khảo HyperLogLog - http://antirez.com/news/75
* Dùng PFADD, PFCOUNT
* Dùng nginx làm load balancer
* Dùng supervisord để quản lý (bật, tắt) các process redis, python, nginx
* Dùng apache benchmark (ab) hoặc wrk phải đạt > 2000 requests/giây
* Dùng ansible để deploy toàn bộ project này lên 1 server ubuntu 14.04 (tự cài virtualbox để test)


