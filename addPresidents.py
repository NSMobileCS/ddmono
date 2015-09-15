from nsdjangoden.models import President

#presidents to add list
pl = [('Abe Lincoln', 'Mary Lincoln'),
      ('George Washington', 'Martha Washington'),
      ('Bill Clinton', 'Hillary Clinton'),
      ('Ronald Reagan', 'Nancy Reagan'),
      ('Thomas Jefferson', 'Martha_Jefferson'),
      ('Jimmy Carter', 'Rosalynn_Carter'),
]


def putPrestoDB(pl=pl, default_votes=0):
    for m, f in pl:
        presimg = '_'.join(m.split(' '))+'.jpg'
        p = President(pres_name=m, presimg=presimg, realfirstlady=f)
        fll = [i[-1] for i in pl if i[-1] != f]
        p.save()
        for firstlady in fll:
            flimg = '_'.join(firstlady.split(' '))+'.jpg'
            p.firstlady_set.create(lady_name=firstlady, image=flimg, votes=default_votes)
            p.save()

def chkPresinDB(pl=pl):
    all_pres = President.objects.all()
    try:
        assert len(all_pres) > 4
    except AssertionError:
        return "Database Error - objects not returned"
    for p in all_pres:
        print(p)
        print(p.firstlady_set.all(), end='\n\n'+'_*_'*5+'\n\n')
        try:
            assert 1 < p.firstlady_set.count() < len(pl)
        except AssertionError:
            return "Database Error - firstlady_set len out of range"
    return "OK"


# President model attrib's are ('pres_name', 'presimg', 'realfirstlady')


# class FirstLady(models.Model):
#     president = models.ForeignKey(President)
#     lady_name = models.CharField(max_length=80)
#     image = models.CharField(max_length=80)
#     votes = models.IntegerField(default=0)

if __name__ == '__main__':
    print("Data to add: ")
    print(pl, '\n')
    y = input("Add this data? Enter (y/n): ")
    if y.lower() == 'y':
        putPrestoDB()
        print("Making sure data in DB")
        print("DB Data Result: %s" % chkPresinDB())
    elif y.lower == 'n':
        exit()