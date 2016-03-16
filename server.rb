require 'webrick'
server = WEBrick::HTTPServer.new(
  :Port => 5000, # a server's port
  :DocumentRoot => File.join(Dir.pwd, "/scripts") # a folder with scripts
)
server.start