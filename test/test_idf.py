

def test_tf_idf(test_client, captured_templates):
    input_text = "After learning about data handling, datasets, loader and transforms in PyG, it’s time to implement our first graph neural network!"
    data       = {"text_field": input_text}
    response   = test_client.post('/tf-idf', data=data)

    assert response.status_code == 200
    


def test_tf_idf_blank_input(test_client, captured_templates):
    input_text = ""
    data       = {"text_field": input_text}
    response   = test_client.post('/tf-idf', data=data)

    assert response.status_code == 409

    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == 'tf_idf.html'
    assert "info" in context
    assert context["info"] == "Please enter text"