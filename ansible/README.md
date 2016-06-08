# Cai dat may ao vagrant

1. Download vagrant
    ```bash
    $ https://www.vagrantup.com/downloads.html
    ```
2. Cai dat may ao vagrant

    ```bash
$ vagrant init ubuntu/trusty64
    ```

3. Cau hinh may ao  theo file Vagrantfile

    ```bash
    $ vagrant up
    ```

4. Tai may chu chay cac lenh

    ```bash
    $ ssh-keygen

    $ cd ~/.ssh

    $ > known_hosts
    ```

5. Vao vagrant bang lenh

    ```bash
    $ vagrant ssh
    ```
6. coppy id_rsa.pub vao vagrant tai thu muc ~/.ssh/authorized_keys

7. Muon vao lai vagrant thi chay lenh  

    ```bash
    $ ssh vagrant@192.168.33.10
    ```

8. Ve may chu, copy doan code vao /opt/ansible/

9. Sau do chay lenh

    ```bash
    $ ansible-playbook -u vagrant -i hosts site.yml
    ```
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


