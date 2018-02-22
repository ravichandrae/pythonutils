class Utils:
  @staticmethod
  def sort_file(file_path, delimiter):
      with open(file_path) as f:
        with open('Programs1.txt', encoding='utf-8', mode='w') as new_file:
          lines = feed_file.readlines()
          for line in sorted(lines, key=lambda line: line.split(u'\u0001')[0]):
            new_file.write(line)
