CC = g++
CFLAGS = -g
OUT_DIR = build
OBJS = main.o
OUT_OBJS=$(addprefix $(OUT_DIR)/,$(OBJS))

main: ${OBJS}
	${CC} ${CFLAGS} -o run ${OUT_OBJS}

%.o: src/%.cpp
	${CC} ${CFLAGS} $< -c -o ${OUT_DIR}/$@

clean:
	rm ${OUT_DIR}/*.o run