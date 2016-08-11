```bash
$ git clone https://github.com/quangns/test.git

$ cd test

$ git remote rename origin github
```

#Tạo file script, viết code & commit

```bash
$ echo "print 'Hello world!'" > hello_world.py

$ git add hello_world.py

$ git commit -m "Add: Hello world script"

$ git push -u github master
```
#Mấy lệnh git hay dùng

*Lấy code mới về*
```bash
$ git pull --rebase gitlab master
```
*Push code ở local lên*
```bash
$ git push origin master
```
*Xem trạng thái git hiện tại*
```bash
$ git status
```
*Xem commit log*
```bash
$ git log
```
*Add các file vào git*
```bash
$ git add --all
```

Dùng:
Abc: Message
hoặc:
Abc: Message

Description
Trong đó:
Abc là Add, Mod(ify), Ref(actoring), Fix, Rem(ove) và Rea(dability)
Ví dụ:
Add: New function to rule the world
Mod: Add women factor in Domination.ruleTheWorld()
Ref: Extract empathy stuff to an abstract class
Fix: RUL-42 or #42 Starvation need to be initialised before Energy to avoid the nullpointer in People
Rem: freeSpeech is not used anymore
Rea: Removed old TODO and extra space in header
Dùng pre-commit để fix mấy lỗi coding & writing style

Cài pre-commit
$ sudo pip install pre-commit
Test & tự động fix mấy lỗi trình bày cơ bản:
$ pre-commit run --files nguyen_sy_quang/
