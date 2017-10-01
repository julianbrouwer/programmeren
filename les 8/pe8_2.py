def monopolyworp():
    import random
    eerste = random.randrange(1,7)
    tweede = random.randrange(1,7)
    optellen = eerste + tweede

    if eerste == tweede:
        print('{} + {} = {} (dubbel)'.format(eerste, tweede, optellen))
        eerste = random.randrange(1, 7)
        tweede = random.randrange(1, 7)
        optellen = eerste + tweede
        print('{} + {} = {} (dubbel)'.format(eerste, tweede, optellen))
        if eerste==tweede:
            eerste = random.randrange(1, 7)
            tweede = random.randrange(1, 7)
            optellen = eerste + tweede
            print('{} + {} = (direct naar gevangenis)'.format(eerste, tweede))

    else:
        print('{} + {} = {}'.format(eerste, tweede, optellen))

monopolyworp()