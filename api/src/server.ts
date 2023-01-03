import { Server, Socket } from 'socket.io'
import { ClientToServerEvents, InterServerEvents, ServerToClientEvents, SocketData } from './types';

const server = new Server<
    ClientToServerEvents,
    ServerToClientEvents,
    InterServerEvents,
    SocketData
>(8000);

let pid = -1;
console.info("Server started on port 8000")

server.on("connection", (socket: Socket<ClientToServerEvents, ServerToClientEvents>) => {
    const { id } = socket

    socket.join("room")
    socket.to("room").emit("clientJoin", { id, pid: (pid++).toString() })
    socket.on('disconnect', () => { pid-- })

    socket.on("keyPress", ({ key }) => {
        console.info(`Client [id=${id}] pressed [key=${key}]`);
        server.to("room").emit("keyPress", { key, id });
    })
});

