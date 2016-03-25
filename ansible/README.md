# Cai dat may ao vagrant

# Cau hinh may ao  theo file Vagrantfile

# Yeu cau: Viết 1 web app chạy ở port 80, nhận request HTTP request bất kỳ, đếm và trả ra số lượng unique user agent hiện tại (theo từng ngày)

Yêu cầu:

* Dùng flask, redis
* Tham khảo HyperLogLog - http://antirez.com/news/75
* Dùng PFADD, PFCOUNT
* Dùng nginx làm load balancer
* Dùng supervisord để quản lý (bật, tắt) các process redis, python, nginx
* Dùng apache benchmark (ab) hoặc wrk phải đạt > 2000 requests/giây
* Dùng ansible để deploy toàn bộ project này lên 1 server ubuntu 14.04 (tự cài virtualbox để test)


