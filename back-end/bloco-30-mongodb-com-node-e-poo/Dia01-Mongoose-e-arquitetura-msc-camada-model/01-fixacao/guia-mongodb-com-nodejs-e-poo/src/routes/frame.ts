import { Router } from 'express';
import FrameController from '../controllers/Frame';
import FrameModel from '../models/Frame';
import FrameService from '../services/Frame';

const route = Router();

​
const frame = new FrameModel();
const frameService = new FrameService(frame);
const frameController = new FrameController(frameService);

route.post('/frame', (req, res) => frameController.create(req, res));
route.get('/frame/:id', (req, res) => frameController.readOne(req, res));
route.get('/frame', (req, res) => frameController.read(req, res));
route.put('/frame/:id', (req, res) => frameController.update(req, res));
route.delete('/frame/:id', (req, res) => frameController.read(req, res));


export default route;