import { Server, Socket } from 'socket.io'
import { ClientToServerEvents, InterServerEvents, ServerToClientEvents, SocketData } from './types';

const server = new Server<
    ClientToServerEvents,
    ServerToClientEvents,
    InterServerEvents,
    SocketData
>(8000);

server.on("connection", (socket: Socket<ClientToServerEvents, ServerToClientEvents>) => {
    const { id } = socket

    socket.join("room")
    server.to("room").emit("clientJoin", { id });
    socket.on("disconnect", () => {
        server.to("room").emit("clientLeave", { id });
    });

    socket.on("keyPress", ({ key }) => {
        console.info(`Client [id=${id}] pressed [key=${key}]`);
    })
});

