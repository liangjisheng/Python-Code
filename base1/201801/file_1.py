
fn = "a.txt";
fp = open(fn, "r");
print("reading position: ", fp.tell());

r = fp.read(20);
print("have read \"" + r + "\"");
print("reading position: ", fp.tell());

r = fp.read(20);
print("have read \"" + r + "\"");
print("reading position: ", fp.tell());

fp.close();