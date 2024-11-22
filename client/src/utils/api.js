import axios from "axios";

const API = axios.create({
    baseURL: process.env.REACT_APP_API_URL, // Backend URL
});
export default API;

export const fetchTasks = async () => {
  const response = await API.get("/tasks");
  return response.data;
};