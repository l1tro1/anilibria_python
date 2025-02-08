from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement


# Monkeypatch т.к. clear() не всегда корректно работает с элементами VueJS и ReactJS
def clear_input(self) -> None:
    """
    Очищает текстовое поле ввода.

    Эта функция использует сочетание клавиш "Ctrl + A" для выделения всего текста в поле ввода,
    а затем удаляет его с помощью клавиши "Delete".

    Не возвращает значения.

    :return: None
    """
    self.send_keys(Keys.CONTROL + "a")
    self.send_keys(Keys.DELETE)


def xpath(self):
    script = """
    function getElementXPath(element) {
        var paths = [];
        while (element.nodeType === Node.ELEMENT_NODE) {
            var siblingIndex = 1;
            var sibling = element.previousSibling;
            while (sibling) {
                if (sibling.nodeType === Node.ELEMENT_NODE && sibling.tagName === element.tagName) {
                    siblingIndex++;
                }
                sibling = sibling.previousSibling;
            }
            paths.unshift(element.tagName + '[' + siblingIndex + ']');
            element = element.parentNode;
        }
        return paths.length ? '/' + paths.join('/') : null;
    }
    return getElementXPath(arguments[0]);
    """
    return self.parent.execute_script(script, self)


WebElement.clear_input = clear_input
WebElement.xpath = xpath
