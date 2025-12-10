def main():
    c1 = Catalog("Main catalog")
    c1.add_product(Product("Redmi Note 11", 3000000, 200))
    c1.add_product(Product("HUAWEI D16", 10000000, 100))
    c1.add_product(Product("MACBOOK AIR", 11000000, 100))
    while True:
        print("===MENU===")
        print("1.Mahsulot Royhti")
        print("2.Mahsulot Qoshish")
        print("3.buyurtma Berish")
        print("4.Buyurtmalar Royxati")
        print("5.Qidirish")
        print("6.EXIT")
        try:
            choice = int(input("Tanlang: "))
        except ValueError:
            print("Faqat son kiriting!")
            continue

        if choice == 1:
            for p in c1.get_list():
                print(p.info())

        elif choice == 2:
            print("Yangi mahsulot kiritish:")
            name = input("Nomi: ")
            price = int(input("Narxi: "))
            qty = int(input("Soni: "))
            c1.add_product(Product(name, price, qty))
            print("Mahsulot qo'shildi")

        elif choice == 3:
            name = input("Qaysi mahsulot: ")
            product = c1.search(name)
            if product:
                qty = int(input("Nechta: "))
                if qty <= product.qty:
                    product.qty -= qty
                    Order(product, qty)
                    print(" Buyurtma qabul qilindi")
                else:
                    print("Omborda yetarli mahsulot yo‘q")
            else:
                print(" Topilmadi")

        elif choice == 4:
            if not Order.orders:
                print("Buyurtmalar yo‘q")
            else:
                for o in Order.orders:
                    print(o)

        elif choice == 5:
            name = input("Qidirilayotgan nom: ")
            p = c1.search(name)
            if p:
                print("Topildi:", p.info())
            else:
                print("Topilmadi")

        elif choice == 6:
            print("Dastur tugadi")
            break

        else:
            print("Noto'g'ri tanlov!")
main()