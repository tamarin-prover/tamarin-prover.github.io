# Starting ports: occupied ports are skipped without stopping other servers.
# Example: make drafts PORT=4100 LIVERELOAD_PORT=35800
HOST ?= 127.0.0.1
PORT ?= 4000
LIVERELOAD_PORT ?= 35729

.PHONY: default drafts

drafts: JEKYLL_FLAGS = --drafts

default drafts:
	@ruby -rsocket -e '\
	  host = ARGV.shift; \
	  sockets = ARGV.shift(2).map do |value|; \
	    first = Integer(value, 10); \
	    abort "Port must be between 1 and 65535" unless (1..65535).cover?(first); \
	    socket = nil; \
	    (first..65535).each do |port|; \
	      begin; \
	        socket = TCPServer.new(host, port); \
	        break; \
	      rescue Errno::EADDRINUSE, Errno::EACCES; \
	      end; \
	    end; \
	    socket || abort("No available port at or above #{first}"); \
	  end; \
	  port, reload_port = sockets.map { |socket| socket.addr[1].to_s }; \
	  puts "Serving at http://#{host}:#{port} (LiveReload: #{reload_port})"; \
	  sockets.each(&:close); \
	  exec "bundle", "exec", "jekyll", "serve", "--host", host, \
	    "--port", port, "--livereload", "--livereload-port", reload_port, *ARGV; \
	' '$(HOST)' '$(PORT)' '$(LIVERELOAD_PORT)' $(JEKYLL_FLAGS)
