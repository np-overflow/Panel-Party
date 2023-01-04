import { Server, Socket } from 'socket.io'
import { ClientToServerEvents, InterServerEvents, ServerToClientEvents, SocketData } from './types';
import express, { Express } from 'express';
import { createServer } from 'http';

const app: Express = express()
    , server = createServer(app)
    , io = new Server<
        ClientToServerEvents,
        ServerToClientEvents,
        InterServerEvents,
        SocketData
    >(server);

server.listen(8000, () => {
    console.info('⚡️ [server]: Server is running at http://localhost:8000')
});

let pid = -1;

io.on("connection", (socket: Socket<ClientToServerEvents, ServerToClientEvents>) => {
    const { id } = socket

    socket.join("room")
    socket.to("room").emit("clientJoin", { id, pid: (pid++).toString() })
    socket.on('disconnect', () => { pid-- })

    socket.on("keyPress", ({ key }) => {
        console.info(`Client [id=${id}] pressed [key=${key}]`);
        io.to("room").emit("keyPress", { key, id });
    })
});

