# ── Stage 1: Build ──────────────────────────────────────────────────────────
FROM node:20-alpine AS builder
 
WORKDIR /app
 
# Copy dependency files first (better layer caching — only reinstalls
# node_modules when package.json actually changes)
COPY package*.json ./
RUN npm install
 
# Copy the rest of the source and build
COPY . .
RUN npm run build
# Output is in /app/dist
 
 
# ── Stage 2: Serve ───────────────────────────────────────────────────────────
# Use a lightweight nginx image — the final image won't contain Node.js
# or node_modules at all, keeping it small (~25MB vs ~500MB)
FROM nginx:alpine AS production
 
# Copy the compiled assets from the builder stage
COPY --from=builder /app/dist /usr/share/nginx/html
 
# Copy our custom nginx config (handles SPA client-side routing)
COPY nginx.conf /etc/nginx/conf.d/default.conf
 
EXPOSE 80
 
CMD ["nginx", "-g", "daemon off;"]
 