
print(type(1));
print(type(2000));
print(type(9999999999999));
print(type(1.0));
print(type(1 + 12j));
print();

print("test %%d: %d" %10);
print("test %%f: %f" %10);
print("test %%f: %f" %10.1);
print("test %%e: %e" %6.78000E+10);
print("test %%E: %E" %6.78000E+10);
print("test %.2f" %25.10101010101);

# 尽管python可以处理非常大的数，但如果遇到无法处理的大数是将返回inf
print(2e304 * 1234567890);
print(4023 - 22.4);
print("%0.3f" %30.00123);
print("%0.3f" %30.00163);
print("%0.3f" %30.1778);
print("%0.3f" %30.1113);
print();

print("%d %o" %(10, 10));
print("%d %x %X" %(10, 10, 10));