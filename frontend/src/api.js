import axios from 'axios'

// VITE_API_URL is injected at build time (set it in Vercel's project env
// vars to your deployed Render backend URL). Falls back to localhost so
// `npm run dev` keeps working unchanged.
const baseURL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000/api'

const API = axios.create({
  baseURL,
  timeout: 20000,
});
export default API;
