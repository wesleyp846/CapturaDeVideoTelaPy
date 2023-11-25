# Captura de video tela PY
&nbsp;

Script para captura a tela em formato de vídeo com Python
---


&nbsp;
> Pré-code
> > virtual environment

    pip install numpy pyautogui opencv-python keyboard
&nbsp;


&nbsp;
> Funcionalidades
&nbsp;

1. Inicia a captura de vídeo da tela inteira e em cores
2. Grava um vídeo MP4 *sem áudio* com a taxa de quadros definida pela variável `fps`
3. A variável `codec` define a extenssão do arquivo de vídeo
4. Finaliza a gravação ao pressionar `ESC`
5. Salva o arquivo de vídeo como `capturePy.mp4`

&nbsp;
> Uso
&nbsp;

Execute o script Python para iniciar a gravação.

Pressione `ESC` no teclado para interromper a qualquer momento.

&nbsp;

### Implementação

Utiliza pyautogui para capturar os frames da tela e opencv para compor o vídeo a partir dos frames utilizando codecs de vídeo.

A taxa de quadros e resolução são configuradas no início.

&nbsp;
> Créditos
&nbsp;

Código inicial fornecido pela [Hashtag Treinamentos](https://www.youtube.com/watch?v=Hsx2Nhr0Mmo&list=WL&index=8).

Documentação e melhorias adicionadas por [Wesley Pereira](https://github.com/wesleyp846)

&nbsp;
> Licença
MIT
