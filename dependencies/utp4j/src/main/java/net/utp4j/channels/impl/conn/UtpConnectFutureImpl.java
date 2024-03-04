/* Copyright 2013 Ivan Iljkic
*
* Licensed under the Apache License, Version 2.0 (the "License"); you may not
* use this file except in compliance with the License. You may obtain a copy of
* the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
* WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
* License for the specific language governing permissions and limitations under
* the License.
*/
package net.utp4j.channels.impl.conn;

import java.io.IOException;

import net.utp4j.channels.futures.UtpConnectFuture;
/**
 * Hide implementation details.
 * @author Ivan Iljkic (i.iljkic@gmail.com)
 *
 */
public class UtpConnectFutureImpl extends UtpConnectFuture {
	
	public UtpConnectFutureImpl() throws InterruptedException {
		super();
	}
	/**
	 * Releases semaphore and sets return values.
	 * @param exp if exception occured, null is possible.
	 */
	public void finished(IOException exp) {
		this.exception = exp;
		this.isDone = true;
		semaphore.release();
	}

}
