
#/usr/bin/env python

from functools import partial;
import tk;

root = tk.Tk();
MyButton = partial(tk.Button, root, fg = 'white', bg = 'blue');
b1 = MyButton(text = 'Button 1');
b2 = MyButton(text = 'Button 2');
qb = MyButton(text = 'QUIT', bg = 'red', command = root.quit);
b1.pack();
b2.pack();
qb.pack(fill = tk.X, expand = True);
root.title('PFAs!');
root.mainloop();