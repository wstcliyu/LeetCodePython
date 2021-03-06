"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.ls = []
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf = [' '] * n
        if (len(self.ls) > 0):
            if len(self.ls) >= n:
                buf += self.ls[:n]
                self.ls = self.ls[n:]
                return n
            else:
                buf += self.ls.copy()
                self.ls.clear()
        x = 4
        while len(buf) < n and x == 4:
            chars = []
            x = read4(chars)
            if x + len(buf) <= n:
                buf += chars
            else:
                self.ls = chars[n-len(buf):]
                buf += chars[:n-len(buf)]
                return n
        return len(buf)


    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        idx = 0
        while n > 0:
            # read file to buf4
            buf4 = [""] * 4
            l = read4(buf4)
            # if no more char in file, return
            if not l:
                return idx
            # write buf4 into buf directly
            for i in range(min(l, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx