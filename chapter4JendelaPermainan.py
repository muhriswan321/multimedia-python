import pygame

pygame.init()


# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Memuat gambar
image = pygame.image.load('onepiece.jpg')
# Memuat suara
sound = pygame.mixer.Sound('result.wav')

# Loop utama permainan
# Loop utama permainan dengan animasi
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi
    x += 5
    if x > 800:
        x = 0

    # Menggambar gambar di posisi baru
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))

    # Memutar suara
    sound.play()

    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()