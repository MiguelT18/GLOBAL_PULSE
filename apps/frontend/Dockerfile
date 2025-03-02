# Fase 1: Construcción de la aplicación
FROM node:22.14.0-alpine AS builder

# Habilitar PNPM dentro del contenedor
RUN corepack enable && corepack prepare pnpm@latest --activate

# Establecer directorio de trabajo en el contenedor
WORKDIR /src/app

# Copiar el package.json y verificar si PNPM está configurado
COPY apps/frontend/package.json ./package.json

# Comprobar si PNPM está definido en packageManager, si no, agregarlo
RUN if ! grep -q '"packageManager":' package.json; then \
  echo '{' > temp.json && \
  echo '  "packageManager": "pnpm@10.5.2",' >> temp.json && \
  tail -n +2 package.json >> temp.json && \
  mv temp.json package.json; \
  fi

# Verificar si pnpm-lock.yaml existe en el host, si no, generarlo en Docker
RUN if [ ! -f pnpm-lock.yaml ]; then \
  pnpm install --no-frozen-lockfile; \
  fi

# Copiar el código del frontend dentro del contenedor
COPY apps/frontend ./apps/frontend

# Construir la aplicación Next.js dentro del contenedor
RUN cd apps/frontend && pnpm build

# Fase 2: Servir la aplicación con una imagen ligera
FROM node:22.14.0-alpine AS runner
WORKDIR /app

# Instalar PNPM nuevamente en la imagen final
RUN corepack enable && corepack prepare pnpm@latest --activate

# Copiar solo lo necesario desde la fase de build
COPY --from=builder /src/app/apps/frontend/.next ./apps/frontend/.next
COPY --from=builder /src/app/apps/frontend/public ./apps/frontend/public
COPY --from=builder /src/app/apps/frontend/node_modules ./apps/frontend/node_modules
COPY --from=builder /src/app/apps/frontend/package.json ./apps/frontend/package.json
COPY --from=builder /src/app/pnpm-lock.yaml ./pnpm-lock.yaml

# Exponer el puerto de Next.js
EXPOSE 3000

# Comando de inicio en producción
CMD ["pnpm", "--dir", "apps/frontend", "start"]
