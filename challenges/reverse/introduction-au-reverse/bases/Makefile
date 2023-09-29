CC=gcc
CFLAGS=
LDFLAGS=
EXEC=bases

all: $(EXEC).o
	$(CC) -o $(EXEC) $(EXEC).c $(LDFLAGS)

$(EXEC).o: $(EXEC).c
	$(CC) -o $(EXEC).o -c $(EXEC).c $(CFLAGS)

clean:
	rm *.o