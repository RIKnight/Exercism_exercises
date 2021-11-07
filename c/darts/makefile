### If you wish to use extra libraries (math.h for instance),
### add their flags here (-lm in our case) in the "LIBS" variable.

LIBS = -lm

###
CFLAGS  = -std=c99
CFLAGS += -g
CFLAGS += -Wall
CFLAGS += -Wextra
CFLAGS += -pedantic
CFLAGS += -Werror
CFLAGS += -Wmissing-declarations
CFLAGS += -DUNITY_SUPPORT_64

ASANFLAGS  = -fsanitize=address
ASANFLAGS += -fno-common
ASANFLAGS += -fno-omit-frame-pointer

.PHONY: test
test: tests.out
	@./tests.out

.PHONY: memcheck
memcheck: test/*.c *.c *.h
	@echo Compiling $@
	@$(CC) $(ASANFLAGS) $(CFLAGS) *.c test/vendor/unity.c test/*.c -o memcheck.out $(LIBS)
	@./memcheck.out
	@echo "Memory check passed"

.PHONY: clean
clean:
	rm -rf *.o *.out *.out.dSYM

tests.out: test/*.c *.c *.h
	@echo Compiling $@
	@$(CC) $(CFLAGS) *.c test/vendor/unity.c test/*.c -o tests.out $(LIBS)
