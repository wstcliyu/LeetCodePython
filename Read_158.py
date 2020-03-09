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
class Read_158:
    def __init__(self):
        self._buf4Size = 0
        self._buf4Ptr = 0
        self._buf4 = [''] * 4
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        size = 0
        while size < n:
            while size < n and self._buf4Ptr < self._buf4Size:
                buf[size] = self._buf4[self._buf4Ptr]
                size += 1
                self._buf4Ptr += 1
            if self._buf4Ptr == self._buf4Size:
                self._buf4Ptr = 0
                self._buf4Size = read4(self._buf4)
                if self._buf4Size == 0:
                    break
        return size
        
        