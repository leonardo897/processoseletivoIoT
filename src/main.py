"""
Semáforo Inteligente com Travessia de Pedestres - Implementação em MicroPython

Este módulo implementa uma máquina de estados não-bloqueante para controle
de semáforo com funcionalidade de travessia de pedestres.
"""

import machine
import time

# ============================================================
# CONFIGURAÇÃO DE HARDWARE (PINOS)
# ============================================================
RED_LED = 13        # LED vermelho do semáforo
YELLOW_LED = 12     # LED amarelo do semáforo
GREEN_LED = 14      # LED verde do semáforo
PEDESTRIAN_BUTTON = 15  # Botão de solicitação de travessia
BUZZER = 27         # Buzzer para alerta sonoro

# ============================================================
# CONFIGURAÇÃO DE TEMPORIZAÇÃO (milissegundos)
# ============================================================
GREEN_TIME = 5000           # 5 segundos de verde para veículos
YELLOW_TIME = 2000          # 2 segundos de amarelo
RED_TIME_PEDESTRIAN = 4000  # 4 segundos de vermelho com pedestre
BUZZER_DURATION = 500       # 500ms de alerta sonoro
BUZZER_INTERVAL = 200       # 200ms entre bips do buzzer
DEBOUNCE_TIME = 50          # 50ms para debounce do botão

# ============================================================
# DEFINIÇÃO DOS ESTADOS DO SEMÁFORO
# ============================================================
class TrafficLightState:
    """Máquina de estados do semáforo"""
    GREEN = "GREEN"                         # Tráfego fluindo
    YELLOW = "YELLOW"                       # Atenção, vai fechar
    RED = "RED"                             # Veículos parados
    PEDESTRIAN_REQUESTED = "PEDESTRIAN_REQ" # Pedestre solicitou travessia
    PEDESTRIAN_CROSSING = "PEDESTRIAN_CROSS" # Pedestre atravessando

# ============================================================
# INICIALIZAÇÃO DOS COMPONENTES
# ============================================================
def setup_hardware():
    """Configura todos os pinos de I/O do sistema"""
    
    # LEDs como saídas digitais
    red_led = machine.Pin(RED_LED, machine.Pin.OUT)
    yellow_led = machine.Pin(YELLOW_LED, machine.Pin.OUT)
    green_led = machine.Pin(GREEN_LED, machine.Pin.OUT)
    
    # Botão como entrada com pull-up interno
    button = machine.Pin(PEDESTRIAN_BUTTON, machine.Pin.IN, machine.Pin.PULL_UP)
    
    # Buzzer como saída digital
    buzzer = machine.Pin(BUZZER, machine.Pin.OUT)
    
    # Estado inicial: todos LEDs desligados
    red_led.off()
    yellow_led.off()
    green_led.off()
    buzzer.off()
    
    return red_led, yellow_led, green_led, button, buzzer

# ============================================================
# CONTROLE DOS LEDS
# ============================================================
def update_leds(red_led, yellow_led, green_led, state):
    """Controla quais LEDs acendem baseado no estado atual"""
    
    # Desliga todos os LEDs primeiro
    red_led.off()
    yellow_led.off()
    green_led.off()
    
    # Acende o LED correspondente ao estado
    if state == TrafficLightState.GREEN:
        green_led.on()
    elif state == TrafficLightState.YELLOW:
        yellow_led.on()
    elif state in [TrafficLightState.RED, 
                   TrafficLightState.PEDESTRIAN_REQUESTED,
                   TrafficLightState.PEDESTRIAN_CROSSING]:
        red_led.on()

# ============================================================
# CONTROLE DO BUZZER (ALERTA SONORO NÃO-BLOQUEANTE)
# ============================================================
class SoundAlert:
    """Gerencia alertas sonoros do buzzer de forma não-bloqueante"""
    
    def __init__(self, buzzer_pin):
        self.buzzer = buzzer_pin
        self.active = False
        self.last_toggle = 0
        self.buzzer_state = False
        self.start_time = 0
        self.total_duration = 0
        
    def start(self, duration_ms=BUZZER_DURATION):
        """Inicia um alerta sonoro"""
        self.active = True
        self.start_time = time.ticks_ms()
        self.total_duration = duration_ms
        self.last_toggle = self.start_time
        self.buzzer_state = True
        self.buzzer.on()
        
    def update(self):
        """Atualiza o estado do buzzer (deve ser chamada no loop principal)"""
        if not self.active:
            return
            
        current_time = time.ticks_ms()
        
        # Verifica se o alerta terminou
        if time.ticks_diff(current_time, self.start_time) >= self.total_duration:
            self.buzzer.off()
            self.active = False
            return
        
        # Alterna o buzzer a cada BUZZER_INTERVAL ms
        if time.ticks_diff(current_time, self.last_toggle) >= BUZZER_INTERVAL:
            self.buzzer_state = not self.buzzer_state
            if self.buzzer_state:
                self.buzzer.on()
            else:
                self.buzzer.off()
            self.last_toggle = current_time

# ============================================================
# LEITURA DO BOTÃO COM DEBOUNCE
# ============================================================
class ButtonDebounce:
    """Gerencia leitura de botão com debounce por software"""
    
    def __init__(self, button_pin):
        self.button = button_pin
        self.last_state = True  # Pull-up: HIGH = não pressionado
        self.last_time = 0
        self.pressed = False
        
    def update(self):
        """Atualiza o estado do botão (deve ser chamada no loop principal)"""
        self.pressed = False
        current_state = self.button.value()
        current_time = time.ticks_ms()
        
        # Detecta borda de descida (botão pressionado)
        if self.last_state == 1 and current_state == 0:
            if time.ticks_diff(current_time, self.last_time) > DEBOUNCE_TIME:
                self.pressed = True
                self.last_time = current_time
        
        self.last_state = current_state

# ============================================================
# MÁQUINA DE ESTADOS PRINCIPAL
# ============================================================
def run_traffic_light():
    """Função principal: executa a máquina de estados do semáforo"""
    
    # Inicializa hardware
    red_led, yellow_led, green_led, button_pin, buzzer_pin = setup_hardware()
    
    # Inicializa objetos de controle
    alert = SoundAlert(buzzer_pin)
    button = ButtonDebounce(button_pin)
    
    # Estado inicial
    current_state = TrafficLightState.GREEN
    state_time = time.ticks_ms()
    pedestrian_requested = False
    
    print("Smart Traffic Light - System Started ")
    print(f"Initial state: {current_state}")
    
    # ============================================================
    # LOOP PRINCIPAL (NÃO-BLOQUEANTE)
    # ============================================================
    while True:
        current_time = time.ticks_ms()
        
        # Atualiza leitura do botão (debounce)
        button.update()
        
        # Atualiza alerta sonoro (não-bloqueante)
        alert.update()
        
        # Verifica acionamento do pedestre
        if button.pressed and current_state == TrafficLightState.GREEN:
            pedestrian_requested = True
            print("Pedestrian button pressed!")
        
        # ============================================================
        # TRANSIÇÕES DE ESTADO
        # ============================================================
        
        if current_state == TrafficLightState.GREEN:
            # Verde para veículos
            update_leds(red_led, yellow_led, green_led, current_state)
            
            # Se pedestre solicitou OU tempo esgotou, vai para amarelo
            if pedestrian_requested or time.ticks_diff(current_time, state_time) >= GREEN_TIME:
                current_state = TrafficLightState.YELLOW
                state_time = current_time
                print(f"State transition: GREEN -> YELLOW")
                
        elif current_state == TrafficLightState.YELLOW:
            # Amarelo: atenção
            update_leds(red_led, yellow_led, green_led, current_state)
            
            if time.ticks_diff(current_time, state_time) >= YELLOW_TIME:
                if pedestrian_requested:
                    current_state = TrafficLightState.PEDESTRIAN_CROSSING
                    print(f"State transition: YELLOW -> PEDESTRIAN_CROSSING")
                    alert.start(BUZZER_DURATION)
                else:
                    current_state = TrafficLightState.RED
                    print(f"State transition: YELLOW -> RED")
                state_time = current_time
                
        elif current_state == TrafficLightState.RED:
            # Vermelho normal (sem pedestre)
            update_leds(red_led, yellow_led, green_led, current_state)
            
            if time.ticks_diff(current_time, state_time) >= RED_TIME_PEDESTRIAN:
                current_state = TrafficLightState.GREEN
                state_time = current_time
                print(f"State transition: RED -> GREEN")
                
        elif current_state == TrafficLightState.PEDESTRIAN_CROSSING:
            # Vermelho para travessia de pedestre
            update_leds(red_led, yellow_led, green_led, current_state)
            
            if time.ticks_diff(current_time, state_time) >= RED_TIME_PEDESTRIAN:
                current_state = TrafficLightState.GREEN
                state_time = current_time
                pedestrian_requested = False
                print(f"State transition: PEDESTRIAN_CROSSING -> GREEN")
        
        # Pequena pausa para evitar consumo excessivo de CPU
        time.sleep_ms(10)


# ============================================================
# PONTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    try:
        run_traffic_light()
    except KeyboardInterrupt:
        print("\nSystem stopped by user")
    except Exception as e:
        print(f"Unexpected error: {e}")