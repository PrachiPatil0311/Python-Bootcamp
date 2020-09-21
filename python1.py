# an application to design zodiac signs
next = True
while next == True:
    print(''' From all these Zodiac Signs 
    1) Aries
    2) Taurus
    3) Gemini
    4) Cancer
    5) Leo
    6) Virgo
    7) Libra
    8) Scorpio
    9) Sagittarius
    10) Capricon
    11) Aquarius
    12) Pisces
    ''')

    s= int(input("Pick your sign number and Press Enter"))
    print(s)

    if s==1:
        print("This is not the day to either sell or buy property. Your reluctance in spending money on something you accord a lower priority may not be right. A new project will proceed smoothly as you get help from all quarters. Good will power in sticking to the exercise regime will help you in coming back in shape. ")
    elif s==2:
        print("Your mood swings can make you miss a profitable opportunity, so do something about it. You will be able to put across your points effectively on the professional front. Be considerate of a family member in all your domestic decisions. Tread carefully while discussing a property issue. ")
    elif s==3:
        print("Moneywise, you will find yourself more secure now, than before. Good diet and regular exercise will keep you both physically and mentally robust. You may have to share the burden of domestic chores. Those into buying and selling property must focus on discounts.  ")
    elif s==4:
        print("Money will not be a problem for you, so shop till you drop! It may be difficult to make a client accept your views on the professional front. Good physical condition will make strenuous activities, a child’s play. Good returns are foreseen from a rented property.")
    elif s==5:
        print("Despite the fact that you're feeling better than you have in a while, right now is not the time to go out and celebrate. A family youngster may make you proud by his or her achievement. This is a favourable day to seal a property deal. Your professional skills are likely to be acknowledged at work. You will have enough to purchase a major household item. ")
    elif s==6:
        print("Today is a great day to try a new food, hobby, sport, or adventure that you have always been just a little to scared to try before.It is time you turned your attention to saving by becoming more careful of your spending. You will be able to give a good account of yourself by solving workplace problems. ")
    elif s==7:
        print(" You need to keep moving even if you don't know exactly where you're going.An outdoor activity is likely to give you a chance for sweating out. A child may need guidance, so spare some time for him or her.")
    elif s==8:
        print("You have mastered an immense challenge that few people could have handled, but you might be feeling like no one noticed!  Students appearing for examinations or competitions can heave a sigh of relief. You may need to plan a journey in the coming few days. A property deal shows all signs of turning favourable.")
    elif s==9:
        print("What you need now is to be surrounded by people who get you, the people who use the same shorthand you use. Chance to earn big money may present itself to those running their own business. Home remedies come in real handy for those suffering from minor ailments.")
    elif s==10:
        print("Spend time with people who live a different lifestyle. Get a glimpse of what their biggest issues, goals, and concerns are.On the financial front, a new source of income is likely to be tapped soon that may get your coffers brimming! Successfully completing an assigned job will give you the edge at work.")
    elif s==11:
        print("This might seem like a typical day early on, but as each hour goes by, you could start to see more and more mysterious actions and events cropping up.You may choose to wait for better investment options, before committing your money. New dimensions open up on the professional front as you handle more than one project.")
    elif s==12:
        print(" A relationship that you thought was broken beyond all repair still has some life in it. Figure out how you can put it on the road to recovery. Financially, your position remains sound and opportunities to earn materialise. Adopting a disciplined life and change in lifestyle will help in restoring energy and health.")
    else:
        print("This does not correspond to a Zodiac Sign")

    next = True if input("\n Shall we do it again?(Y/N)")== 'Y' else False
