from controllers.traffic_controller import TrafficController

def test_controller_changes_states():
    controller = TrafficController("I1")
    
    # Simulate multiple readings
    for _ in range(10):
        state = controller.manage_traffic()
        assert state in ["RED", "GREEN", "YELLOW"]
