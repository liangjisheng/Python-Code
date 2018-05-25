
a = ("first", "second", "third");
b = (a, "b's second element");

print(a);
print(b);

print("%s" %b[1]);
print("%s" %b[0][0]);
print("%s" %b[0][1]);
print("%s" %b[0][2]);

# 创建一个元素的元素，必须在该元素后面加一个逗号
single_element_tuple = ("the sole element", );
print();

menu_specials = {"breakfast":"sausage and eggs",
"lunch":"split pea soup and garlic bread",
"dinner":"2 hot dogs and onion rings"};

print(menu_specials);
print("%s" %menu_specials["breakfast"]);
print("%s" %menu_specials["lunch"]);
print("%s" %menu_specials["dinner"]);
print(menu_specials.get("breakfast"));
print(menu_specials.get("lunch"));
print(menu_specials.get("dinner"));

# keys()方法要求字典以视图的方式返回所有键，
# values()方法也将以视图的形式返回所有的值
hungry = menu_specials.keys();
print(hungry);
print(list(hungry));

starving = menu_specials.values();
print(starving);
print(list(starving));