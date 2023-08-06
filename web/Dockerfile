FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile

COPY . .

RUN yarn build

EXPOSE 8080

CMD [ "http-server", "dist" ]