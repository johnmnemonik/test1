# тест test1
при пере сохранение записи supply3 и supply4 вылетает ошибка, не правильный процент
округление происзодило в большую сторону, 10,60 --> 11, 7.82 --> 8 
для входа в админку john:loginn1984

просто алгоритм отписан в test1_raw.py там 2 реализации

округление происходит в большую сторону, 10,60 --> 11, 7.82 --> 8  check_proc_max()
округление происходит в меньшую сторону, 10,60 --> 10, 7.82 --> 7  check_proc_min())