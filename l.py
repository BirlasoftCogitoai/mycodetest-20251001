version: '3.8'

services:
  auth_service:
    build:
      context: ./auth_service
    ports:
      - "5000:5000"
    environment:
      - SECRET_KEY=your_secret_key
    networks:
      - app-network

networks:
  app-network:
    driver: bridge