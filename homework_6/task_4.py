import smtplib
help(smtplib)
smtp_object = smtplib.SMTP('smtp.gmail.com')
smtp_object.starttls()
smtp_object.login('julia5767675@gmail.com', 'neverland96')
help(smtp_object.sendmail)
smtp_object.sendmail(from_addr='julia5767675@gmail.com', to_addrs='el.piankova@gmail.com', msg='I did it! by Julia Kravchuk')
smtp_object.quit()