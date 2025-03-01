# videorecorter
import os
from moviepy import VideoFileClip

def recortar_video(input_file, output_file, start_time, end_time):
    # Carregar o vídeo
    video = VideoFileClip(input_file)
    
    # Recortar o vídeo
    video_recortado = video.subclipped(start_time, end_time)
    
    # Salvar o vídeo recortado
    video_recortado.write_videofile(output_file, codec="libx264")

# Exemplo de uso
input_video = r"D:\[ÁLGEBRA LINEAR] O _CURSO COMPLETO_ em 40 Exercícios Resolvidos (ÍNDICE NO INÍCIO, RESUMO NO FINAL!).mp4"  # Caminho do vídeo original
output_video = "Capítulo 5 (Subespaços Vetoriais).mp4"  # Caminho para o vídeo recortado
def tempo_para_segundos(horas=0, minutos=0, segundos=0):
    # Verifica se algum valor é zero e converte corretamente
    if horas < 0 or minutos < 0 or segundos < 0:
        raise ValueError("Os valores de horas, minutos e segundos não podem ser negativos.")

    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

start = tempo_para_segundos(1,27,6)  # Início do recorte em segundos
end = tempo_para_segundos(2,0,57)    # Fim do recorte em segundos
recortar_video(input_video, output_video, start, end)


recortar_video(input_video, output_video, start, end)
output_video = "Capítulo 7 (Diagonizáveis).mp4"  # Caminho para o vídeo recortado

start = tempo_para_segundos(2,35,15)  # Início do recorte em segundos
end = tempo_para_segundos(3,13,26)    # Fim do recorte em segundos

recortar_video(input_video, output_video, start, end)