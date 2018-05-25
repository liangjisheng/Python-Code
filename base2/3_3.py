
slice_me = ("The", "next", "time", "we", "meet", "drinks", "are", "on", "me");
print(slice_me);
slice_tuple = slice_me[5:9];
print(slice_tuple);

slice_list = list(slice_me);
print(slice_list);
slice_list1 = slice_list[5:9];
print(slice_list1);

slice_this_string = "The next time we meet, drinks are on me";
sliced_string = slice_this_string[5:9];
print(slice_this_string);
print(sliced_string);
print();

living_room = ("rug", "table", "chair", "TV", "dustbin", "shelf");
apartment = [];
# 结果是向列表中增加了一个分层的序列
apartment.append(living_room);
print(apartment);

apartment = [];
apartment.extend(living_room);
print(apartment);
print();

alphabet = ['a', 'b', 'b', 'c', 'a', 'd', 'e'];
print(alphabet);
alph2 = set(alphabet);
print(alph2);