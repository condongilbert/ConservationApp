import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:5000", // Backend URL
});

export const fetchTasks = async () => {
  const response = await API.get("/tasks");
  return response.data;
};