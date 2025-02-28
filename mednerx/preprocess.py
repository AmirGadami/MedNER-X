import re



class TextProcessor:

    def parse_annotated_text(self, line):
        parts = line.strip().split('\t')
        annotations = []
        if len(parts)< 3:
            return None
        text = parts[2]
        matches = re.finditer('<category="(.*?)">(.*?)</category>',text)

        for match in matches:
            entity_type, entity_text = match.groups()
            start,end = match.start(2),match.end(2)
            annotations.append((entity_text,entity_type,start,end))

        clean_text = re.sub(r'<category="(.*?)">(.*?)</category>',r'\2', text)

        return clean_text,annotations
